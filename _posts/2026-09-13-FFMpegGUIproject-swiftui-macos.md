---
layout: post
title:  "FFMpegGUI - GUI wrapper for ffmpeg. SwiftUI app to analyze, convert, heal and resample / remux media files on macOS"
author: dave
date:   2026-09-13 17:48:29 +0200
categories: [macOS, Media, SwiftUI]
tags: [macOS, Media, SwiftUI, Tools]
published: true
---

![FFMpegGUI for macOS](../../assets/img/projects/FFMpegGUI/FFMpegGUI-First-Overall-MainView-03.png){: width="85%" }

# FFMpegGUI

A High-Performance, Sandbox-Compliant macOS Audio/Video Processing Suite

- Platform: macOS 14.0+
- Language: Swift 5.10+
- License: MIT
- Technology: Swift / SwiftUI + Objective-C + XPC + FFmpeg

## Table of Contents
1. Executive Overview & Vision
2. High-Level System Architecture
3. The Sandbox Challenge: Security-Scoped Bookmarks
4. XPC Service Architecture & IPC Topology
5. Core Subsystems & Module Breakdown
   • Boot Sequence & PyScraper Subsystem
   • PillView & Custom NSViewRepresentable Tokenizer
   • Dynamic Multi-Pane Layout & Watchdog Subsystem
6. Data Flow & Serialization (NSSecureCoding)
7. Dependencies & Package Topology
8. Setup, Build, and Installation Guide
9. Diagnostic, Logging & Unit Testing Paradigms

⸻

## 1. Executive Overview & Vision

FFMpegGUI is an advanced, native macOS application designed to simplify high-performance media validation, inspection, and transcoding. By pairing a responsive, modern SwiftUI-based user interface with a decoupled, privileged XPC Service, the application offers a unique combination of native Mac-centric user experience and raw command-line/C-bound encoding efficiency.

Traditional FFmpeg wrappers on macOS run into critical design bottlenecks, particularly concerning App Sandbox compliance and main-thread interface blocking during heavy I/O operations. This project solves these paradigms through:

- Strict Sandbox Isolations: Bypassing filesystem boundaries cleanly via secure-scoped bookmarks.
- Architectural Separation of Concerns: Isolating FFmpeg runtimes and dynamic C-library loading (via CFFMpeg) into a separate helper process.
- Visual Command Customization: Empowering power-users with an NSTextView rendering pipeline that visually parses complex terminal CLI flags into stylized, crisp vector graphics dynamically.

## 1.1 ffmpeg Binaries vs. ffmpeg API Libraries
FFMpegGUI comes with two different strategies of how to use the ffmpeg system to work with media files.

Basically you have the choice between using the official ffmpeg binaries to work with or you can switch to using the (custom compiled - you can do this yourself if you like) ffmpeg C API libraries to analyze and work with media files. Both ways offer its unique advantages. Switching between this two approaches is seemless and you can litrally do this by the click of a button.

FFMpegGUI features a configuration profile manager so you can persistently save you FFMpegGUI configuration and switch between them easylly and on the fly.

## 2. High-Level System Architecture
The application is structured as a decentralized, multi-process environment containing three core layers:

### 2.1. Host GUI Process (FFMpegGUI): 
Contains the SwiftUI views, local user defaults, State/Observable objects, drag-and-drop orchestration, and live AVPlayer playback previews.

### 2.2. Privileged XPC Service (FFMpegGUIXPCService): 
A sandboxed helper running as an on-demand launchd service. It executes low-level FFmpeg queries, analyzes stream metadata, and converts raw files on dedicated background queues.

### 2.3. Low-Level Native Libraries (FFMpegSwiftLib, FFMpegSwiftManagerLib, CFFMpeg): 
Swift wrappers interfacing with native dynamically linked (or statically built) FFmpeg frameworks (libavcodec, libavformat, libavutil, etc.).

#### System Interaction Topology

```bash
+--------------------------------------------------------------------------------+
|                             macOS Kernel Sandbox                               |
|                                                                                |
|   +---------------------------------+  Security   +------------------------+   |
|   |         MAIN GUI APP            |  Scoped     |     XPC HELPER SERVICE |   |
|   |  - SwiftUI Core Interface       |  Bookmarks  |  - FFMpegXPCService    |   |
|   |  - Drag & Drop Delegates        +------------>|  - libavcodec wrapper  |   |
|   |  - Watchdog Monitor & Heartbeat |             |  - Integrity Checker   |   |
|   |  - TokenTextView Renderer       |    NSXPC    |  - File Sanitizer      |   |
|   +----------------+----------------+ Connection  |  - Progress Updates    |   |
|                    ^                |<===========>|                        |   |
|                    |                |             +------------------------+   |
|                    v                |                                          |
|         +-------------------+       |                                          |
|         |  parameters.json  |       |                                          |
|         |  AppSupport Directory     |                                          |
|         +-------------------+       |                                          |
+-------------------------------------+------------------------------------------+
```

## 3. The Sandbox Challenge: Security-Scoped Bookmarks

Running an FFmpeg utility inside a Sandboxed macOS application presents a unique challenge: filesystem visibility. Under Apple’s security policy, a sandboxed app cannot read arbitrary files unless explicitly authorized by user interaction (via system open panels or drag-and-drop actions).

### Solving the Inode Trap (file:///.file/id=)
When dragging items into a SwiftUI interface, the system occasionally provides path references formatted as file-reference URLs (file:///.file/id=...). Attempting to extract relative directories or passing these directly to standard POSIX file systems will result in access errors.

To overcome this, FFMpegGUI intercepts the item provider in its custom MediaDropDelegate:

```swift
guard let rawNSURL = item as? NSURL ?? (item as? Data).flatMap({ NSURL(absoluteURLWithDataRepresentation: $0, relativeTo: nil) }),
      let pathNSURL = rawNSURL.filePathURL else {
    NSLog("❌ Failed to resolve standard file path URL.")
    return
}
```

Using rawNSURL.filePathURL forces the operating system to resolve low-level inode references into normalized POSIX filesystem paths, preparing them for security authorization.

### Cryptographic Security Bookmarks
To grant the background XPC Service access to a file, the Main App converts authorized POSIX paths into cryptographic security-scoped bookmark payloads (Data). These are safely serialized, passed across the XPC boundary, and re-materialized on the service side:

```swift
let bookmarkData = try pathNSURL.bookmarkData(
    options: [], 
    includingResourceValuesForKeys: nil,
    relativeTo: nil
)
```

On the receiving end of a deep-link or XPC action, the boundary resolves these tokens using:

```swift
let sandboxSecuredURL = try URL(
    resolvingBookmarkData: bookmarkData,
    options: [], 
    relativeTo: nil,
    bookmarkDataIsStale: &isStale
)

guard sandboxSecuredURL.startAccessingSecurityScopedResource() else {
    // Handle sandboxing denial by kernel
    return
}
defer {
    sandboxSecuredURL.stopAccessingSecurityScopedResource()
}
```

## 4. XPC Service Architecture & IPC Topology

The connection between the Host GUI and the background processing engine is managed by NSXPCConnection. This provides bidirectional type-safe communication.

Vending the Interface Protocols
The XPC listener, defined in main.swift, is driven by the class FFMpegXPCServiceDelegate, conforming to NSXPCListenerDelegate. It exposes FFMpegXPCServiceProtocol while configuring strict security rules:

```swift
class FFMpegXPCServiceDelegate: NSObject, NSXPCListenerDelegate {
    
    let exportedObject = FFMpegXPCService()
    
    /// This method is where the NSXPCListener configures, accepts, and resumes a new incoming NSXPCConnection.
    func listener(_ listener: NSXPCListener, shouldAcceptNewConnection newConnection: NSXPCConnection) -> Bool {
        
        let interface = NSXPCInterface(with: (any FFMpegXPCServiceProtocol).self)
        
        newConnection.exportedInterface = interface
        newConnection.exportedObject = exportedObject

        let interfaceRemote = NSXPCInterface(with: (any ImportProgressListenerLibNG).self)
        newConnection.remoteObjectInterface = interfaceRemote

        // Resuming the connection allows the system to deliver more incoming messages.
        newConnection.resume()
        
        // Returning true from this method tells the system that you have accepted this connection. If you want to reject the connection for some reason, call invalidate() on the connection and return false.
        return true
    }
}

// Create the delegate for the service.
let delegate = FFMpegXPCServiceDelegate()

// Set up the one NSXPCListener for this service. It will handle all incoming connections.
let listener = NSXPCListener.service()
listener.delegate = delegate

// Resuming the serviceListener starts this service. This method does not return.
listener.resume()
```

Because custom Swift objects (like MediaDetails) are sent across the boundary, the standard collection interfaces must be registered to support security subclass boundaries, ensuring that only expected types are serialized during remote method invocations.

## 5. Core Subsystems & Module Breakdown

Boot Sequence & PyScraper Subsystem
When FFMpegGUI boots, it executes a multi-phase validation logic:

```bash
[App Launch]
     |
     v
[Perform Startup Check] ------------------------> (File Found: parameters.json)
     |                                                      |
     v (No cached JSON file)                                v
[Run Bundled Python Scraper]                         [Load Parameters]
     |                                                      |
     +-------> Scrapes FFmpeg command parameters            |
     |         to application support folder                v
     v                                              [Launch Main UI]
[Flush to Disk & Reload]
```

This sequence is managed by FFmpegDataManager.swift:

- It checks for the existence of parameters.json in the user's ApplicationSupport directory.
- If missing, it invokes a background Process targeting a bundled script: generate_ffmpeg_params_json_gemini.py.
- Because macOS GUI processes do not automatically inherit user shell paths, the manager injects standard Homebrew and local binary search paths into the process environment before launching:

```swift
var env = ProcessInfo.processInfo.environment
env["PATH"] = "/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/homebrew/bin"
process.environment = env
```

### PillView & Custom NSViewRepresentable Tokenizer
One of the most innovative design choices in FFMpegGUI is the visualization of FFmpeg parameters. Instead of raw terminal flags, users view structured command "pills" inside an editor.

This is implemented inside PillView.swift via TokenTextView (wrapping an AppKit NSTextView in NSViewRepresentable).

```bash
"ffmpeg -vcodec h264 -acodec mp3"
           |
           v (Token Search Engine)
+----------------------------+
|  "-vcodec" -> [ PillView ] |
|  "-acodec" -> [ PillView ] |
+----------------------------+
           |
           v (ImageRenderer Core Graphics Render)
"ffmpeg [ -vcodec ] h264 [ -acodec ] mp3"
```


### 1. Rendering SwiftUI to Native Images:
Using macOS 13+ ImageRenderer, SwiftUI visual hierarchies are rasterized on the fly into retina-crisp NSImage instances:

```swift
let renderer = ImageRenderer(content: PillView(text: token))
   renderer.scale = NSScreen.main?.backingScaleFactor ?? 2.0
```

### 2. NSTextAttachment Integration:
The rasterized image is embedded directly into the rich text representation:

```swift
let attachment = NSTextAttachment()
   attachment.image = image
   attachment.bounds = CGRect(x: 0, y: -4, width: image.size.width, height: image.size.height)
   let attachmentString = NSAttributedString(attachment: attachment)
   result.replaceCharacters(in: foundRange, with: attachmentString)
```

### Dynamic Multi-Pane Layout & Watchdog Subsystem
The application leverages a classic Mac three-pane split layout. The dynamic sidebar (SidebarDetailsView.swift) operates as an inspection center divided into four dynamic sections:

1. Media Preview: Integrates a real-time native player overlay.
2. Media Details: Provides clear, formatted file information:
   - File Size (formatted using human-readable bytes).
   - Sample Rates, FPS, Resolutions, and precise Duration formatting.
   
3. Batch Task Details: Displays multi-item import progress, overall operation progress, and time estimates.
4. XPCService Details (Watchdog Subsystem):
A dedicated background loop periodically pings the XPC Helper. The GUI monitors this connection, displaying real-time health metrics:
	- Service Status: Connection verification.
	- Missed Pings: Visual indicator if the XPC queue blocks.
	- PID tracker: Retrieves and tracks the process identifier of the helper.
	- Crash Auto-Recovery: If a crash occurs, the watchdog logs the event and automatically re-binds the channel.

## 6. Data Flow & Serialization (NSSecureCoding)

To safely transmit rich models across processes without standard text encoding overhead, MediaDetails.swift implements the standard NSSecureCoding protocol:

```swift
@objc(MediaDetails)
public final class MediaDetails: NSObject, NSSecureCoding, Identifiable, ObservableObject, @unchecked Sendable, @preconcurrency MediaDetailsProvider  {

    public static var supportsSecureCoding: Bool { true }
    
    public func encode(with coder: NSCoder) {
        coder.encode(id, forKey: "id")
        coder.encode(filename, forKey: "filename")
        coder.encode(format, forKey: "format")
        coder.encode(duration, forKey: "duration")
        coder.encode(hasVideo, forKey: "hasVideo")
        coder.encode(videoCodec, forKey: "videoCodec")
        // ... (Nested fields)
        coder.encode(mediaConversionConfig, forKey: "mediaConversionConfig")
    }
}
```

This ensures that even when your backend processes encounter untrusted inputs or corrupt file metadata payloads, the IPC interface blocks malformed object structures at the serialization boundary.

## 7. Dependencies & Package Topology

The FFMpegGUI ecosystem is structured as modular, reusable Swift Packages to ensure clean code segregation:

```bash
                           '+---------------------------+
                           |        FFMpegGUI          |
                           |  (Main SwiftUI App Space) |
                           +-------------+-------------+
                                         |
               +-------------------------+-------------------------+
               |                                                   |
               v                                                   v
+-----------------------------+                     +-----------------------------+
| FFMpegGUIXPCServiceLib      |                     | FFMpegSwiftManagerLib       |
| (XPC Protocol Interfaces)   |                     | (Core Configs & Delegates)  |
+--------------+--------------+                     +--------------+--------------+
               |                                                   |
               +-------------------------+-------------------------+
                                         |
                                         v
                            +-----------------------------+
                            |     FFMpegSwiftLib          |
                            | (FFmpeg Object wrappers)    |
                            +--------------+--------------+
                                           |
                                           v
                            +-----------------------------+
                            |        CFFMpeg              |
                            |  (Native C Framework Clang) |
                            +-----------------------------+
```

### Core Packages Description

- CFFMpeg: Low-level Clang module-map interfacing directly with raw dynamically compiled headers from the FFmpeg framework.
- FFMpegSwiftLib: Swift interfaces exposing classes for format streams, audio/video channels, frame accessors, and low-level FFmpeg context setups.
- FFMpegSwiftManagerLib: High-level managers implementing common configurations, global task records, the security-scoped sandbox model, and standard serialization logic.
- FFMpegGUIXPCServiceLib: Contains XPC service implementations, listeners, service protocols, and client callbacks.

## 8. Setup, Build, and Installation Guide

Follow these steps to configure, build, and test the sandbox-secured application:

### Prerequisites:
- macOS Sonoma (14.0) or newer.
- Xcode 15.3 or newer.
- Swift 5.10+.
- FFmpeg Frameworks: Installed via Homebrew or compiled statically / dynamically as frameworks in your library path.


### Install FFmpeg with shared libraries via Homebrew
```bash
brew install ffmpeg
```

### !!! Cloning and Fetching Submodules - COMMING SOON !!!
```bash
git clone --recurse-submodules https://github.com/yourusername/FFMpegGUI.git
cd FFMpegGUI
```

#### Entitlements & Sandboxing Requirements
Because the app utilizes sandboxing with an XPC service, ensure your Target Entitlements in Xcode are configured correctly:

**FFMpegGUI.entitlements**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.assets.user-selected.read-write</key>
	<true/>
	<key>com.apple.security.files.user-selected.read-write</key>
	<true/>
	<key>com.apple.security.files.bookmarks.app-scope</key>
	<true/>
	<key>com.apple.security.scripting-targets</key>
	<dict>
		<key>com.apple.Terminal</key>
		<array>
			<string>com.apple.Terminal.send</string>
		</array>
	</dict>
</dict>
</plist>
```

**FFMpegGUIXPCService.entitlements**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.files.bookmarks.app-scope</key>
	<true/>
	<key>com.apple.security.inherit</key>
	<true/>
</dict>
</plist>
```

**Building the Project**
1. Open FFMpegGUI.xcodeproj in Xcode.
2. Select your development team to allow system capabilities for Sandboxing and IPC communication.
3. Build the primary target (FFMpegGUIApp). Xcode will automatically compile package dependencies, compile the nested helper XPC Service, copy it into the app's Contents/XPCServices subdirectory, and sign the bundle with your developer identity.

## 9. Diagnostic, Logging & Unit Testing Paradigms

FFMpegGUI includes diagnostic utilities to trace, isolate, and debug complex processing pipelines across sandbox boundaries.

### Diagnostic Logging Subsystem
All background events, system errors, and command-line parsing steps are captured by a centralized logging framework (DebugLogger):

- Console Output: Streamed directly via standard macOS Unified Logging API (os_log).
- Disk persistence: Extracted using a specialized FFFileLogger that logs outputs into your secure application directory.
- Visual Log Viewer: The main UI features a searchable log console panel displaying infos, warnings, errors, and debug statements in real-time.

### Integrated Swift Testing Suite
Unit tests leverage the modern Swift Testing framework, ensuring concurrency safety and sandbox compliance.

```swift
import Testing
@testable import FFMpegGUI
import Foundation

@Suite("FFmpeg Subsystem Tests")
struct FFmpegSubsystemTests {
    
    @Test("Verify Human-Readable File Sizes")
    func testFileSizeConversion() throws {
        let sizeInBytes = 1_048_576 // 1 MB
        let converted = sizeInBytes.humanReadableSize(type: .megabyte)
        #expect(converted == "1.00 MB")
    }
    
    @Test("Verify Safe Sandbox Token Resolution")
    func testSandboxBookmarkValidity() async throws {
        let tempDirectory = FileManager.default.temporaryDirectory
        let targetFile = tempDirectory.appendingPathComponent("test_stream.mp4")
        
        // Ensure dummy file exists
        try "dummy_data".write(to: targetFile, atomically: true, encoding: .utf8)
        defer { try? FileManager.default.removeItem(at: targetFile) }
        
        // Generate bookmark
        let bookmarkData = try targetFile.bookmarkData(
            options: [],
            includingResourceValuesForKeys: nil,
            relativeTo: nil
        )
        
        var isStale = false
        let resolvedURL = try URL(
            resolvingBookmarkData: bookmarkData,
            options: [],
            relativeTo: nil,
            bookmarkDataIsStale: &isStale
        )
        
        #expect(!isStale)
        #expect(resolvedURL.lastPathComponent == "test_stream.mp4")
    }
}
```

This document serves as an exhaustive structural guide for developers, security auditors, and users. For additional information or questions, please open an issue in the primary project repository.


## 10. Credits and References
- [https://ffmpeg.org](https://ffmpeg.org){:target="_blank" rel="noopener"} - ffmpeg

### Author
- Kim David Hauser (jetedonner)
- kim@kimhauser.ch
- https://kimhauser.ch

### REMARK:
- GITHUB Repo is not yet public but will be comming soon - stay tuned!
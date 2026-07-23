# System Architecture

## Introduction

System architecture describes how computer hardware, software, the operating system, memory, CPU, and networking work together to perform tasks.

---

# The OSI Model

![OSI Model](https://media.geeksforgeeks.org/wp-content/uploads/20250117112545142665/OSI-Model-.webp)

The Open Systems Interconnection (OSI) model is a conceptual framework that explains how data moves from one device to another through seven different layers.

## OSI Layers

| Layer           | Function                                           |
| --------------- | -------------------------------------------------- |
| 7. Application  | Provides network services to applications.         |
| 6. Presentation | Formats, encrypts, and compresses data.            |
| 5. Session      | Creates and manages communication sessions.        |
| 4. Transport    | Ensures reliable data delivery using TCP or UDP.   |
| 3. Network      | Routes packets using IP addresses.                 |
| 2. Data Link    | Uses MAC addresses and detects errors.             |
| 1. Physical     | Transmits bits through cables or wireless signals. |

---

## Why the OSI Model Isn't Used in Production

The OSI model is mainly used for learning networking concepts. Modern networks use the TCP/IP model because it is simpler and matches how the Internet actually works.

---

# TCP/IP Model

![TCP/IP Model](https://th.bing.com/th/id/R.349e5587a8a663a749cdd7f6b440f998?rik=3X0JQgww4WZQAQ&riu=http%3a%2f%2f1.bp.blogspot.com%2f_FRSoY4n-eek%2fS21qmcKw5UI%2fAAAAAAAAAf4%2fmYCB2024Yrs%2fw1200-h630-p-k-no-nu%2fTCPIP%2bDiagram.jpg&ehk=YA9EDnHKwCnAjgC1WNpLqmofJt6YkIuPMk59tmD8ATA%3d&risl=&pid=ImgRaw&r=0)

| Layer          | Function                                          |
| -------------- | ------------------------------------------------- |
| Application    | User applications and services (HTTP, FTP, SMTP). |
| Transport      | Uses TCP and UDP for communication.               |
| Internet       | Handles IP addressing and routing.                |
| Network Access | Communicates with the physical network hardware.  |

---

# What Happens When You Click an Application

![Computer Architecture](https://blog.autoclicker.com/wp-content/uploads/2025/03/Auto-Click-Macro-How-to-Use-It-for-Gaming-Like-a-Pro.jpg)

1. You click an application on the GUI.
2. The Operating System receives the request.
3. The Kernel processes the request.
4. RAM is allocated.
5. The CPU fetches, decodes, and executes instructions.
6. Addressing modes help the CPU locate data.
7. Device drivers communicate with hardware.
8. If internet access is required, data moves through the TCP/IP stack.
9. The processed result is sent back to the GUI.

---

# Addressing Modes

- Immediate Addressing
- Direct Addressing
- Indirect Addressing
- Register Addressing
- Indexed Addressing

These methods allow the CPU to access memory efficiently.

---

# Flow of an Action Inside the Computer

![System Flow](https://www.techspot.com/articles-info/2000/images/2020-04-06-image.png)

```text
GUI
 ↓
Operating System
 ↓
Kernel
 ↓
Memory (RAM)
 ↓
CPU
 ↓
Storage / Network / Devices
 ↓
Operating System
 ↓
GUI (Output to User)
```

![System Flow](https://d2o2utebsixu4k.cloudfront.net/Structure%20of%20Operating%20System-08e1e18747a445c393999db3e69e77a4.jpg)

---

# Conclusion

Every action performed on a computer passes through several components, including the GUI, operating system, kernel, memory, CPU, and hardware before the final result is displayed. Although the OSI model is useful for understanding networking, real-world systems rely on the TCP/IP model because it is more practical and efficient.

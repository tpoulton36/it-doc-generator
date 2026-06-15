# Project Decisions

## 2026-06-15 - MVP Parser Approach

### Decision

The MVP will use a simple rule-based parser instead of AI.

### Reason

A rule-based parser is free, predictable, easier to test, and good enough for the first version of the product.

Since this project is being bootstrapped with no budget, the first version should avoid paid APIs or services.

### Initial Parser Rules

The parser should recognize simple infrastructure notes such as:

- Server names
- IP addresses
- Operating systems
- Device types
- Basic descriptions

Example input:

```text
Server: DC01
IP: 192.168.1.10
OS: Windows Server 2022
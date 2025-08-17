# pypi-mcp-server
A simple, FastMCP server for PyPI that provides package metadata lookup capabilities to LLMs.

## Features
- Query PyPI package information and metadata
- Support for specific version queries
- Fast and lightweight FastMCP implementation

## Installation

### Prerequisites
- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`

### Using uv (Recommended)
```bash
# Clone the repository
git clone https://github.com/sunil-dhaka/pypi-mcp-server.git
cd pypi-mcp-server

# Install dependencies
uv sync
```

### Using pip
```bash
# Clone the repository
git clone https://github.com/sunil-dhaka/pypi-mcp-server.git
cd pypi-mcp-server

# Install dependencies
pip install fastmcp httpx
```

## How to Use

### 1. Basic Setup
The server provides a single tool `get_package_metadata` that can query PyPI for package information.

### 2. MCP Client Configuration
Add this configuration to your MCP client settings:

```json
"pypi-mcp": {
    "command": "uv",
    "args": ["run", "/absolute/path/to/server.py"]
}
```

Or if using pip:
```json
"pypi-mcp": {
    "command": "python",
    "args": ["/absolute/path/to/server.py"]
}
```

### 3. Available Tools

#### `get_package_metadata`
Retrieves metadata for a PyPI package.

**Parameters:**
- `package` (string, required): The PyPI package name
- `version` (string, optional): Specific version to query

**Returns:**
- Package version
- Description
- Summary
- Project URLs
- Python version requirements

**Example Usage:**
```python
# Get latest package info
result = await get_package_metadata("requests")

# Get specific version info
result = await get_package_metadata("requests", "2.31.0")
```

## Error Handling

The server provides helpful error messages and suggestions for common issues:
- Package not found
- Version not found
- Network connectivity issues
- Invalid package names

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
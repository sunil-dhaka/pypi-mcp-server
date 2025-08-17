# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "fastmcp>=2.11.3",
#     "httpx>=0.28.0",
# ]
# ///

from typing import Optional, Dict, Any
import httpx
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("PyPI Package Metadata Server")

@mcp.tool()
async def get_package_metadata(package: str, version: Optional[str] = None) -> Dict[str, Any]:
    """
    Get PyPI package metadata for a given package name and optional version.
    
    Args:
        package: The PyPI package name
        version: Optional specific version to query
    
    Returns:
        Dictionary containing package metadata or error information
    """
    
    # Construct the PyPI API URL
    if version:
        url = f"https://pypi.org/pypi/{package}/{version}/json"
    else:
        url = f"https://pypi.org/pypi/{package}/json"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            
            if response.status_code == 404:
                if version:
                    return {
                        "error": f"Package '{package}' version '{version}' not found on PyPI",
                        "suggestion": f"Check if the version exists or try without version parameter"
                    }
                else:
                    return {
                        "error": f"Package '{package}' not found on PyPI",
                        "suggestion": "Verify the package name spelling"
                    }
            
            response.raise_for_status()
            data = response.json()
            
            info = data.get("info", {})
            
            return {
                "version": info.get("version", "unknown"),
                "description": info.get("description", "No description available"),
                "summary": info.get("summary", "No summary available"),
                "project_urls": info.get("project_urls", {}),
                "requires_python": info.get("requires_python", "Not specified")
            }
            
    except httpx.RequestError as e:
        return {
            "error": f"Failed to fetch data from PyPI: {str(e)}",
            "suggestion": "Check your internet connection and try again"
        }
    except Exception as e:
        return {
            "error": f"Unexpected error: {str(e)}",
            "suggestion": "Please report this issue"
        }

if __name__ == "__main__":
    mcp.run()

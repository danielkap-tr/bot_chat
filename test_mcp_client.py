
import subprocess
import json
import sys
import os

def run_client():
    # Path to the server script
    server_script = os.path.join(os.getcwd(), 'FastMCP.py')
    
    # Start the server process
    process = subprocess.Popen(
        [sys.executable, server_script],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=sys.stderr,
        text=True,
        bufsize=1
    )

    print("Connected to MCP server.")

    # 1. Initialize
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0"}
        }
    }
    
    print("\n[Client] Sending initialize...")
    process.stdin.write(json.dumps(init_request) + "\n")
    process.stdin.flush()

    # Read initialize response
    response = process.stdout.readline()
    print(f"[Server] {response.strip()}")
    
    # Send initialized notification
    process.stdin.write(json.dumps({
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }) + "\n")
    process.stdin.flush()

    # 2. Call the tool
    print("\n[Client] Calling tool 'inspect_parquet_schema'...")
    tool_call = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "inspect_parquet_schema",
            "arguments": {
                "file_path": "sample.parquet"
            }
        }
    }
    
    process.stdin.write(json.dumps(tool_call) + "\n")
    process.stdin.flush()

    # Read tool response
    # The server might send limits or other messages, but we expect the result next
    # basic reading loop
    while True:
        line = process.stdout.readline()
        if not line:
            break
        try:
            msg = json.loads(line)
            if msg.get("id") == 2:
                print(f"\n[Server Result]:\n{json.dumps(msg, indent=2)}")
                # Check for content
                if "result" in msg and "content" in msg["result"]:
                    for content in msg["result"]["content"]:
                        print(f"\n--- Content ---\n{content['text']}\n---------------")
                break
            else:
                print(f"[Server Message] {line.strip()}")
        except json.JSONDecodeError:
            print(f"[Server Raw] {line.strip()}")

    process.terminate()

if __name__ == "__main__":
    run_client()

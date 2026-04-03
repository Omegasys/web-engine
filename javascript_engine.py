import py_v8

class JavaScriptSandbox:
    def __init__(self):
        self.context = py_v8.create_context()

    def evaluate(self, code):
        try:
            result = py_v8.execute_string(self.context, code)
            return result
        except py_v8.JSException as e:
            return str(e)

    def destroy(self):
        py_v8.release_context(self.context)

def main():
    # Create a sandbox for each script
    sandbox1 = JavaScriptSandbox()
    sandbox2 = JavaScriptSandbox()

    # Execute JavaScript code in the first sandbox
    js_code1 = """
    var x = 10;
    var y = 20;
    function add(a, b) {
        return a + b;
    }
    var result = add(x, y);
    result;
    """
    result1 = sandbox1.evaluate(js_code1)
    print("Result from Sandbox 1:", result1)

    # Execute JavaScript code in the second sandbox
    js_code2 = """
    var a = 5;
    var b = 15;
    function multiply(a, b) {
        return a * b;
    }
    var result = multiply(a, b);
    result;
    """
    result2 = sandbox2.evaluate(js_code2)
    print("Result from Sandbox 2:", result2)

    # Destroy the sandboxes
    sandbox1.destroy()
    sandbox2.destroy()

if __name__ == "__main__":
    main()

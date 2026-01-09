from pyscript import document, display

def finding_average(e): #we put e for event handling.
    num1 = float(document.getElementById("input1").value)
    num2 = float(document.getElementById("input2").value)
    add = num1 + num2 # before getting dividing, we must first add the two numbers. The aritmethic operator used was addition or +
    fanswer = add / 2 # in order to get the average, the arithmetic operator used was division.

    if fanswer >= 75:
        result = f"Average: {fanswer} ✅ You passed! Great job!"
    else:
        result = "Average: {fanswer} ❌ You failed... try harder next time!"

    document.getElementById("avg").textContent = ""
    document.getElementById("avg").textContent = result
    
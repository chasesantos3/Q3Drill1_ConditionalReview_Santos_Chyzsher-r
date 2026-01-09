from js import document, isNaN

def computeAverage():
    s1 = float(document.getElementById('score1').value)
    s2 = float(document.getElementById('score2').value)
    resultDiv = document.getElementById('result')

    # Input validation
    if isNaN(s1) or isNaN(s2) or s1 < 0 or s1 > 100 or s2 < 0 or s2 > 100:
        resultDiv.textContent = "Invalid input."
        resultDiv.className = ""
        return

    # Compute average
    avg = (s1 + s2) / 2

    # Result message
    if avg >= 75:
        resultDiv.textContent = "YOU GET NEW SHOES AND 1K YAY: " + f"{avg:.2f}"
        resultDiv.className = "pass"
    else:
        resultDiv.textContent = "what a loser...: " + f"{avg:.2f}"
        resultDiv.className = "fail"

// Select color input
// Select size input

// When size is submitted by the user, call makeGrid()

function makeGrid() {
    const colNumber = document.getElementById("inputWidth").value
    const rowNumber = document.getElementById("inputHeight").value

    document.getElementById("table_div").removeChild(document.getElementById("pixelCanvas"));

    var gridTable = document.createElement('table');
    gridTable.setAttribute("id", "pixelCanvas")

    for (var rowCounter = 0; rowCounter < rowNumber; rowCounter++) {
        var tr = gridTable.insertRow();

        for (var columnCounter = 0; columnCounter < colNumber; columnCounter++) {
            var td = tr.insertCell();
            td.setAttribute("onClick", "changeCellColor()")
        }
    }

    document.getElementById("table_div").appendChild(gridTable)

}

function changeCellColor(x, y) {
    var clickedCell = event.srcElement
    var selectedColor = document.getElementById("colorPicker").value
    clickedCell.setAttribute("style", "background-color: " + selectedColor + ";")
}
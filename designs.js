// Select size input
var size = document.getElementById('sizePicker');

//create a variable to store the canvas
var gridContainer = document.getElementById('pixelCanvas');

//when the user presses the submit button, capture the value for
//the height and width and call makeGrid()
size.addEventListener('submit', function () {
  event.preventDefault();  //stop the page from constantly reloading
  var height = document.getElementById('inputHeight').value;
  var width = document.getElementById('inputWidth').value;
  makeGrid(height, width);
});

//eventListener at the entire grid container is cascaded down to each td.
//onclick change the cell color to matcn tbe color selected by the user
gridContainer.addEventListener('click', function (e) {
  e.preventDefault();
  var cellColor = document.getElementById('colorPicker').value;
  e.target.style.backgroundColor = cellColor;
});

//make a grid using the height and width values entered by the user
function makeGrid(height, width) {
  var height = document.getElementById('inputHeight').value;
  var width = document.getElementById('inputWidth').value;
  gridContainer.innerHTML = null;
  for (var row = 0; row < height; row++){
    var r = document.createElement('tr');
    gridContainer.appendChild(r);
      for (var cell = 0; cell < width; cell++){
        var c = document.createElement('td');
        r.appendChild(c);
          //
        }
    }
  }

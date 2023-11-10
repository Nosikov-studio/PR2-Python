let x1=0;
let y1=1;
let x2=0;
let y2=1;
let t=0;
let radius=100
let factor=3
let theta


function setup() {
  
  createCanvas(400, 400);
  background(150,150,150);
   

 
}




function draw() {
  
  stroke(255,0,0)
  strokeWeight(1);
  
  fill(255,255,255)
  background(150,150,150);
  factor=+10;
  //circle(mouseX, mouseY, 24)
  for (i=0; i<=360; i++) {
  theta =(PI/180)*i
  x1=radius * cos(theta) + 200;
  y1=radius * sin(theta) + 200;
  
  x2=radius * cos(theta*factor) + 200;
  y2=radius * sin(theta*factor) + 200;
  line(x1, y1, x2, y2)
  }
  
  
  
  
}

/*
let t = frameCount;
  let x = 30 * cos(t * 0.1) + 50;
  let y = 10 * sin(t * 0.2) + 50;
*/
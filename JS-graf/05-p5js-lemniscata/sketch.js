let x1=0;
let y1=1;
let x2=0;
let y2=1;
let t=0;



function setup() {
  
  createCanvas(400, 400);
  background(150,150,150);
   

 
}




function draw() {
  
  stroke(255,0,0)
  strokeWeight(4);
  
  fill(255,255,255)
  
  //circle(mouseX, mouseY, 24)
  
  
  x1=150 * cos(t * 0.1) + 200;
  y1=50 * sin(t * 0.2) + 100;
  
  x2=150 * cos(t * 0.1) + 200;
  y2=50 * sin(t * 0.2) + 100;
  
  t=t+1
  
  
  line(x1, y1, x2, y2)
  
}

/*
let t = frameCount;
  let x = 30 * cos(t * 0.1) + 50;
  let y = 10 * sin(t * 0.2) + 50;
*/
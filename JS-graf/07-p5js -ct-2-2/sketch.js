
let circleX

function setup() {
  
  createCanvas(400, 400);
  
   circleX =100;

 
}

function mousePressed(){
	circleX=0;
}


function draw() {
	
	background(0);
	noStroke(255,0,0)
	strokeWeight(4);  
	fill(255,255,255)
	circleX=circleX+1;
  
	circle(circleX, 150, 24)
  
}

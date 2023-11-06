function setup() {
  
  createCanvas(400, 400);  

  angleMode(DEGREES)

 
}




function draw() {
  background(220);
  push()
  translate(width/2, height/2);
  //rotate(PI/4)
  rotate(180/4)
  rect (0, 0, 100, 100);
  
  pop()

  ellipse (0,0,100,100)

}

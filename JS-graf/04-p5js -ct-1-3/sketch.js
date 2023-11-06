function setup() {
  
  createCanvas(400, 400);
  
   

 
}




function draw() {
	
	background(220, 100, 200);
	fill(0,255,0)
	rect(100,50,25,75)
	line(0,10,400,300)
	
	rectMode(CENTER)
	rect(200,150,150,150)
	
	// альфа-канал (4-й параметр)
	fill(255,0,0, 100)
	ellipse(150, 250, 100, 75)
	// толщина обводки
	fill(0,0,255)
	
	stroke('black')
	strokeWeight(8)
	rect(300,200,25,75)
	
	noStroke()
	
	rect(350,350,70,50)
	
	
  
}

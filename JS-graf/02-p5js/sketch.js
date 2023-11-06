var bg
let x
console.log("Hello,World!!!")

function setup() {  
  console.log('Hi from setup!');
  createCanvas(800, 500);
  x=width/2;
  // bg = loadImage("images/sky.jpg");
  background(200);
  //image(bg, 0, 0);
  //точка
  point(100,100)
  // линия
  line(200, 200, 300, 300)
  // прямоугольник
  rect(400,400, 50, 70)
  // задаем контур
  stroke(0,0,255)
  // задаем заливку
  fill(0,255,0)
  // прямоугольник
  rect(400,100, 50, 70)
  // отключаем контур
  noStroke()
  fill(253,123,224)
  rect(600,200, 50, 70)
  fill(0,0,0)
  // эллипс
  ellipse(50,50,80,100)

  //изменение частоты кадров
  // frameRate(5)
}


function draw() {
  // console.log('Hi from draw!');
  // background(bg);
  
  // translate(random(0, width), random(0, height));
  translate(100, 100)

  stroke(255,0,255)
  line(300, 300, x, 500)
  x+=10
}

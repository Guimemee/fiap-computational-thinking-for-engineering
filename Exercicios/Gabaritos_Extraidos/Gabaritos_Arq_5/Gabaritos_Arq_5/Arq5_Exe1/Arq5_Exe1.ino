int x,y,r;
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Informe valor de 0 a 9, inteiro");
  while(Serial.available()==0);
  x=Serial.read();
  x=x-48;

  y=x%2;

  if(y==0){
    r=x*x;
    Serial.print("Quadrado: ");
    Serial.println(r);
  }
  while(1);
}

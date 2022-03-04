float minha_altura = 1.65;
float ac,ad,au,a;
char p;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Sua altura (exemplo: 1.65) : ");
  while(Serial.available()==0);
  ac=Serial.read();
  ac=ac-48;
  while(Serial.available()==0);
  p=Serial.read();
  while(Serial.available()==0);
  ad=Serial.read();
  ad=ad-48;
  while(Serial.available()==0);
  au=Serial.read();
  au=au-48;
  a=ac+ad/10+au/100;
  
  if(a <= minha_altura)
    Serial.println("Eita! Voce e tao pequeno(a) quanto eu!");

  while(1);
}

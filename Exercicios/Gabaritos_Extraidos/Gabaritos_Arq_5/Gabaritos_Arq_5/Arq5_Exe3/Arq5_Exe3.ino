int meu_peso = 85;
int pc,pd,pu,p;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Seu peso, em 3 digitos: ");
  while(Serial.available()==0);
  pc=Serial.read();
  pc=pc-48;
  while(Serial.available()==0);
  pd=Serial.read();
  pd=pd-48;
  while(Serial.available()==0);
  pu=Serial.read();
  pu=pu-48;
  p=pc*100+pd*10+pu;
  
  if(p != meu_peso)
    Serial.println("Uau! Temos pesos diferentes!");

  while(1);
}

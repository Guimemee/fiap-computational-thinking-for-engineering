int minha_idade = 18;
int id,iu,i;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Sua idade, em 2 digitos: ");
  while(Serial.available()==0);
  id=Serial.read();
  id=id-48;
  while(Serial.available()==0);
  iu=Serial.read();
  iu=iu-48;
  i=id*10+iu;
  
  if(i == minha_idade)
    Serial.println("Legal! Temos a mesma idade!");

  while(1);
}

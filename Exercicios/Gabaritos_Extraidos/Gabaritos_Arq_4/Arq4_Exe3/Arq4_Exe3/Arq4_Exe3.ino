//Declaração de variáveis
int c,d,u,vkm;
float vmil;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Informe a velocidade em km/h: ");
  while(Serial.available()==0);
  c=Serial.read();
  c=c-48;
  while(Serial.available()==0);
  d=Serial.read();
  d=d-48;
  while(Serial.available()==0);
  u=Serial.read();
  u=u-48;

  vkm=c*100+d*10+u;

  vmil=vkm*0.621;

  Serial.print("Velocidade: ");
  Serial.print(vmil);
  Serial.println(" milhas/h");

  while(1);
}

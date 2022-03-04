//Declaração de variáveis
int c,d,u,n;
float v;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Centena: ");
  while(Serial.available()==0);
  c=Serial.read();
  c=c-48;
  Serial.println("Dezena: ");
  while(Serial.available()==0);
  d=Serial.read();
  d=d-48;
  Serial.println("Unidade: ");
  while(Serial.available()==0);
  u=Serial.read();
  u=u-48;

  n=c*100+d*10+u;

  v=n*3.0;
  v=v*1.1;

  Serial.print("Valor da conta: ");
  Serial.println(v);

  while(1);
}

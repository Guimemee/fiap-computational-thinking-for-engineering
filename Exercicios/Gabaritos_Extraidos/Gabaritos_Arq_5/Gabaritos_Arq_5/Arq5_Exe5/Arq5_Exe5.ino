int v1,v2,d;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Digite dois valores inteiros entre 0 e 9: ");
  while(Serial.available()==0);
  v1=Serial.read();
  v1=v1-48;
  while(Serial.available()==0);
  v2=Serial.read();
  v2=v2-48;
  
  if(v1 < v2){
    d=v2-v1;
  }else{
    d=v1-v2;
  }
  
  Serial.print("Diferenca: ");
  Serial.println(d);

  while(1);
}

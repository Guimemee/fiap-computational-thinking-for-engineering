int v;
char s;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Digite um valor inteiro entre 0 e 9 com seu sinal (exemplo -2): ");
  while(Serial.available()==0);
  s=Serial.read();
  while(Serial.available()==0);
  v=Serial.read();
  v=v-48;
  
  if(s == '-'){
    Serial.println("Valor negativo! ");
    Serial.print("Seu modulo: ");
    Serial.println(v);
  }else{
    Serial.println("Valor positivo! ");
    Serial.print("Seu modulo: ");
    Serial.println(v);
  }
  
  while(1);
}

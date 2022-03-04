int A,B,C;
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Lado A:");
  while(Serial.available()==0);
  A=Serial.read();
  A=A-48;
  Serial.println("Lado B:");
  while(Serial.available()==0);
  B=Serial.read();
  B=B-48;
  Serial.println("Lado C:");
  while(Serial.available()==0);
  C=Serial.read();
  C=C-48;

  if(A<B+C && B<A+C && C<A+B){
    if(A==B && B==C){
      Serial.println("Equilatero");
    }else{
      if(A!=B && B!=C && C!=A){
        Serial.println("Escaleno");
      }else{
        Serial.println("Isosceles");
      }
    }
  }else{
    Serial.println("Nao e triangulo!");
  }
  while(1);
}

int N1d,N1u,N1,N2d,N2u,N2,N3d,N3u,N3;
float M;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Nota 1: ");
  while(Serial.available()==0);
  N1d=Serial.read();
  N1d=N1d-48;
  while(Serial.available()==0);
  N1u=Serial.read();
  N1u=N1u-48;
  N1=N1d*10+N1u;
  
  Serial.println("Nota 2: ");
  while(Serial.available()==0);
  N2d=Serial.read();
  N2d=N2d-48;
  while(Serial.available()==0);
  N2u=Serial.read();
  N2u=N2u-48;
  N2=N2d*10+N2u;
  
  Serial.println("Nota 3: ");
  while(Serial.available()==0);
  N3d=Serial.read();
  N3d=N3d-48;
  while(Serial.available()==0);
  N3u=Serial.read();
  N3u=N3u-48;
  N3=N3d*10+N3u;

  M=(N1+N2+N3)/3.0;

  if(M>=7){
    Serial.print("Aprovado com media ");
    Serial.println(M);
  }
  else{
    Serial.print("Reprovado com media ");
    Serial.println(M);
  }
  while(1);
}

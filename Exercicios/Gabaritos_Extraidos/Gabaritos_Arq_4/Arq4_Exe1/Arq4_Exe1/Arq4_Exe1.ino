// programa EXERCÍCIO 1

// declaração de variáveis

int N1,N2,N3,N4,N5;
float M;

void setup() {
  Serial.begin(9600);
}

void loop() {
    Serial.println("Digite o valor da Nota 1:");
    while(Serial.available()==0);
    N1 = Serial.read();
    N1=N1-48;
    Serial.println("Digite o valor da Nota 2:");  
    while(Serial.available()==0);
    N2 = Serial.read();
    N2=N2-48;
    Serial.println("Digite o valor da Nota 3:");  
    while(Serial.available()==0);
    N3 = Serial.read();
    N3=N3-48;
    Serial.println("Digite o valor da Nota 4:");  
    while(Serial.available()==0);
    N4 = Serial.read();
    N4=N4-48;
    Serial.println("Digite o valor da Nota 5:");  
    while(Serial.available()==0);
    N5 = Serial.read();
    N5=N5-48;
    
    M = (N1+N2+N3+N4+N5)/5.0;

    Serial.print("Media: ");
    Serial.println(M);

    while(1);
}

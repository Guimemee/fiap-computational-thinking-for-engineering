#define chC 12
#define chA 11
#define chB 10
#define ledA 4
#define ledB 3
#define ledC 2

bool A,B,C;

void setup() {
  pinMode(chA, INPUT);
  pinMode(chB, INPUT);
  pinMode(chC, INPUT);
  pinMode(ledA, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(ledC, OUTPUT);

  digitalWrite(ledA, LOW);
  digitalWrite(ledB, LOW);
  digitalWrite(ledC, LOW);
}

void loop() {
  C=digitalRead(chC);
  if(C == 1){
    A=digitalRead(chA);
    if(A == 0){
      digitalWrite(ledA, HIGH);
      digitalWrite(ledB, LOW);
    }else{
      digitalWrite(ledA, LOW);
      digitalWrite(ledB, HIGH);
    }
  
    B=digitalRead(chB);
    if(B == 0){
      digitalWrite(ledC, LOW);
    }else{
      digitalWrite(ledC, HIGH);
    }
  }
}

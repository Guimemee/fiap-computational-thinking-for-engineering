#define s1 11
#define s2 9
#define s3 10
#define s4 12
#define mp 3

bool ch1,ch2,ch3,ch4;

void setup() {
  pinMode(s1, INPUT);
  pinMode(s2, INPUT);
  pinMode(s3, INPUT);
  pinMode(s4, INPUT);
  pinMode(mp, OUTPUT);

  digitalWrite(mp, LOW);
}

void loop() {
  ch1=digitalRead(s1);

  if(ch1 == 0){
    digitalWrite(mp, HIGH);
  }

  ch2=digitalRead(s2);

  if(ch2 == 0){
    digitalWrite(mp, LOW);
    delay(3000);
    digitalWrite(mp, HIGH);
  }

  ch3=digitalRead(s3);

  if(ch3 == 0){
    digitalWrite(mp, LOW);
    delay(4000);
    digitalWrite(mp, HIGH);
  }

  ch4=digitalRead(s4);

  if(ch4 == 0){
    digitalWrite(mp, LOW);
    while(1);
  }
}

//Gabarito Exe 1 do Arq 7

int rm,rmc,rmd,rmu;
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Informe a matricula:");
  while(Serial.available()==0);
  rmc=Serial.read();
  rmc = rmc - 48;
  while(Serial.available()==0);
  rmd=Serial.read();
  rmd = rmd - 48;
  while(Serial.available()==0);
  rmu=Serial.read();
  rmu=rmu - 48;
  rm = rmc*100+rmd*10+rmu;
  switch(rm){
    case 94:
      Serial.println("Aluno: Lucas Vigarista");
      Serial.println("Curso: Engenharia");
      Serial.println("Ano: 1º ano");
    break;
    case 95:
      Serial.println("Aluno: Leonardo Charmoso");
      Serial.println("Curso: Musica");
      Serial.println("Ano: 4º ano");
    break;
    case 96:
      Serial.println("Aluno: Vitor Rudimento");
      Serial.println("Curso: Ciencias do Corpo");
      Serial.println("Ano: 3º ano");
    break;
    case 97:
      Serial.println("Aluno: Tiago Cacique");
      Serial.println("Curso: Psicologia");
      Serial.println("Ano: 2º ano");
    break;
    case 98:
      Serial.println("Aluno: Milton Athala");
      Serial.println("Curso: Gastronomia");
      Serial.println("Ano: 1º ano");
    break;
    case 99:
      Serial.println("Aluno: Caboacho Kabo");
      Serial.println("Curso: Letras");
      Serial.println("Ano: 4º ano");
    break;
    case 100:
      Serial.println("Aluno: Kadu Kadon");
      Serial.println("Curso: Ciencias Biologicas");
      Serial.println("Ano: 2º ano");
    break;
    case 101:
      Serial.println("Aluno: Tulio Tanenbaum");
      Serial.println("Curso: Sistemas de Informacao");
      Serial.println("Ano: 3º ano");
    break;
    case 102:
      Serial.println("Aluno: Ana Maria Trevisan");
      Serial.println("Curso: Moda");
      Serial.println("Ano: 1º ano");
    break;
    case 103:
      Serial.println("Aluno: Nubia Thais Picasso");
      Serial.println("Curso: Design de Interiores");
      Serial.println("Ano: 3º ano");
    break;
    default:
      Serial.println("Valor invalido!");
  }
}

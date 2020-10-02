/*
  Clignotement de LED
  Allume une LED pendant 1 seconde, puis l'éteint pendant 1 seconde
  puis le programme se répète indéfiniment

  Cet exemple est dans le domaine public
  Traduction française par X. HINAULT - www.mon-club-elec.fr
 */

void setup() {                
  // initialise la broche 13 en sortie numérique
  // la broche 13 a une LED déjà connectée sur la plupart des cartes Arduino :
  pinMode(13, OUTPUT);    
}

void loop() {
  digitalWrite(13, HIGH);   // allume la LED
  delay(1000);              // ne fait rien pendant 1 seconde
  digitalWrite(13, LOW);    // éteint la LED
  delay(1000);              // ne fait rien pendant 1 seconde
  
}

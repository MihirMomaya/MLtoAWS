function validateForm() {
  var x = document.forms["myForm"]["gre_score"].value;
  if (x == "") {
    alert("GRE Score must be filled!");
    return false;
  }
  if (x<130 || x>340){
  alert ("Gre Score should be in range 130-340");
  return false;
   }
  var y = document.forms["myForm"]["toefl_score"].value;
  if (y == "") {
    alert("Toefl Score must be filled!");
    return false;
  }
  if (y<0 || y>120){
  alert ("Toefl Score should be in range 0-120");
  return false;
   }
  var z = document.forms["myForm"]["university_rating"].value;
  if (z == "") {
    alert("University Rating must be filled!");
    return false;
  }
  if (z<0 || z>5){
  alert ("University Rating Should be in range 0-5");
  return false;
   }
  var a = document.forms["myForm"]["sop"].value;
  if (a == "") {
    alert("SOP Score must be filled!");
    return false;
  }
  if (a<0 || a>5){
  alert ("SOP Score Should be in range 0-5");
  return false;
   }
  var b = document.forms["myForm"]["lor"].value;
  if (b == "") {
    alert("Lor Score must be filled !");
    return false;
  }
  if (b<0 || b>5){
  alert ("Lor Score Should be in range 0-5");
  return false;
   }
  var c = document.forms["myForm"]["cgpa"].value;
  if (c == "") {
    alert("CGPA  must be filled !");
    return false;
  }
  if (c<0 || c>10){
  alert ("CGPA Should be in range 0-10");
  return false;
   }
}
//  Title of app: A2B Converter (Azimuth to Bearing Cnverter)

//  React Native Cmponents
//  Text for title of app on interface and other text titles for data like Azimuth, Bearing 
//  TextInput for azimuth input
//  View for displaying the output bearing
//  Button for the button to press to convert the azimuth to bearing

//  Look of the app (Interface) 
//  At the top the title of the app will be displayed
//  The Text "Azimuth:" with a TextInput box beside it
//  underneath this is
//  A Button with the text "Convert" beside it
//  
//  
//  


// create if-else for DMS
// if (x == <90) {
//     console.log(x.toString().concat{" is equal to "}, y.toString)
// else if (x == 90) {
//     console.log(x.toString().concat{" is equal to "}, y.toString)

// else if (x == >90) && (x == <180)
//     
// else if (x == 180) {
// 
// else if (x == <90) {
//     console.log(x.toString().concat{" is equal to "}, y.toString)
// else if (x == <90) {
//     console.log(x.toString().concat{" is equal to "}, y.toString)
// else if (x == <90) {
//     console.log(x.toString().concat{" is equal to "}, y.toString)
// else if (x == <90) {
//     console.log(x.toString().concat{" is equal to "}, y.toString)

if (azimuth > 0) && (azimuth < 90) {
        bearing = 'S {:^10} W'.format(azimuth)
    else if (azimuth > 90) && (azimuth < 180) {
        bearing = 'N {:^10} W'.format(180 - azimuth)
    else if (azimuth > 180) && (azimuth < 270) {
        bearing = 'N {:^10} E'.format(azimuth - 180)
    else if (azimuth < 360) {
        bearing = 'S {:^10} E'.format(360 - azimuth)
    else if (azimuth == 0) {
        bearing = "DUE SOUTH"
    else if (azimuth == 90) {
        bearing = "DUE WEST"
    else if (azimuth == 180) {
        bearing = "DUE NORTH"
    else if (azimuth == 270) {
        bearing = "DUE EAST"
    else if (azimuth == 360) {
        bearing = "DUE SOUTH"
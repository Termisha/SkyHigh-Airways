import { NgModule } from '@angular/core';
import { MatSnackBarModule } from '@angular/material/snack-bar';  // Import Snackbar module

@NgModule({
  imports: [MatSnackBarModule],
  exports: [MatSnackBarModule]  // Export MatSnackBarModule so it can be used in other components
})
export class SharedModule {}

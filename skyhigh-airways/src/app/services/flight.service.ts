import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FlightService {

  private apiUrl = 'http://localhost:5000/api/search_flights';  // Endpoint

  constructor(private http: HttpClient) {}

  searchFlights(origin: string, destination: string): Observable<any[]> {
//searchFlights(origin: string, destination: string): Observable<any[]> {
    let params = new HttpParams()
      .set('origin', origin)
      .set('destination', destination)
      //.set('travelDate', travelDate)
      // .set('passengers', passengers.toString());

    return this.http.get<any[]>(this.apiUrl, { params });
  }
}

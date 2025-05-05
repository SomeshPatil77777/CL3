import java.rmi.Remote;
import java.rmi.RemoteException;
public interface HotelServiceInterface extends Remote {
boolean bookRoom(String guestName, int roomNumber) throws
RemoteException;
boolean cancelBooking(String guestName) throws RemoteException;
}
import java.rmi.Naming;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            // Look up the RMI server object from the registry
            HotelServiceInterface hotelService = (HotelServiceInterface)
                    Naming.lookup("rmi://localhost/HotelService");

            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.println("\n--- Hotel Booking System ---");
                System.out.println("1. Book a room");
                System.out.println("2. Cancel booking");
                System.out.println("3. Exit");
                System.out.print("Enter your choice: ");
                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume the newline

                switch (choice) {
                    case 1:
                        System.out.print("Enter guest name: ");
                        String guestName = scanner.nextLine();
                        System.out.print("Enter room number: ");
                        int roomNumber = scanner.nextInt();
                        boolean booked = hotelService.bookRoom(guestName, roomNumber);
                        if (booked) {
                            System.out.println("✅ Room booked successfully!");
                        } else {
                            System.out.println("❌ Room booking failed.");
                        }
                        break;

                    case 2:
                        System.out.print("Enter guest name for cancellation: ");
                        String cancelGuestName = scanner.nextLine();
                        boolean canceled = hotelService.cancelBooking(cancelGuestName);
                        if (canceled) {
                            System.out.println("✅ Booking canceled successfully!");
                        } else {
                            System.out.println("❌ Booking cancellation failed.");
                        }
                        break;

                    case 3:
                        System.out.println("Exiting the client application.");
                        System.exit(0);
                        break;

                    default:
                        System.out.println("Invalid choice. Please enter a valid option.");
                }
            }
        } catch (Exception e) {
            System.out.println("An error occurred while connecting to the server:");
            e.printStackTrace();
        }
    }
}

import java.io.IOException;

public class Part1Test {
    public static void main(String[] args) {
        try {
            testPart1();
            System.out.println("Test passed!");
        } catch (AssertionError e) {
            System.err.println("Test failed: " + e.getMessage());
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        }
    }

    public static void testPart1() throws IOException {
        int expected = 0; // TODO: Set expected result
        int result = Part1.solve("inputs/test1.txt");
        assert result == expected : String.format("Expected %d, got %d", expected, result);
    }
}

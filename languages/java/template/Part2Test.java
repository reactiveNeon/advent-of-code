import java.io.IOException;

public class Part2Test {
    public static void main(String[] args) {
        try {
            testPart2();
            System.out.println("Test passed!");
        } catch (AssertionError e) {
            System.err.println("Test failed: " + e.getMessage());
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        }
    }

    public static void testPart2() throws IOException {
        int expected = 0; // TODO: Set expected result
        int result = Part2.solve("inputs/test2.txt");
        assert result == expected : String.format("Expected %d, got %d", expected, result);
    }
}

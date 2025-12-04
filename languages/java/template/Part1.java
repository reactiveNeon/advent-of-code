import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Part1 {
    public static void main(String[] args) {
        try {
            long startTime = System.currentTimeMillis();
            int result = solve("inputs/input.txt");
            long elapsed = System.currentTimeMillis() - startTime;
            System.out.println(result);
            System.err.println("Runtime: " + elapsed + "ms");
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        }
    }

    public static int solve(String inputPath) throws IOException {
        List<String> lines = Files.readAllLines(Path.of(inputPath));

        // TODO: Implement solution
        for (String line : lines) {
            // Process each line
        }

        return 0;
    }
}

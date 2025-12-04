import java.io.File
import kotlin.system.measureTimeMillis

fun solve(inputPath: String): Int {
    val lines = File(inputPath).readLines()

    // TODO: Implement solution
    for (line in lines) {
        // Process each line
    }

    return 0
}

fun main() {
    var result: Int
    val elapsed = measureTimeMillis {
        result = solve("inputs/input.txt")
    }
    println(result)
    System.err.println("Runtime: ${elapsed}ms")
}

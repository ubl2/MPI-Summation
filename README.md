# MPI Array Summation

This Python program demonstrates parallel computation using **MPI (Message Passing Interface)** to calculate the sum of integers in a large array. The array is divided among multiple processes to leverage parallel processing for faster computation.

---

## How It Works

1. **Master-Worker Paradigm**:
   - The **master process (rank 0)** divides the array into chunks and computes its local sum for its chunk.
   - The master distributes the remaining chunks to **worker processes (rank > 0)**.
   - Each worker computes the sum of its chunk and sends the result back to the master.

2. **Final Result**:
   - The master aggregates the sums from all worker processes to compute the total sum of the array.

---

## Prerequisites

- Python 3.x
- `mpi4py` library
- `numpy` library

### Installing Dependencies

1. Install Python:
   - [Download and install Python](https://www.python.org/downloads/).

2. Install required libraries using pip:
   ```bash
   pip install mpi4py numpy
   ```

3. Ensure you have an MPI implementation installed (e.g., OpenMPI or MPICH):
   ```bash
   sudo apt install openmpi-bin openmpi-common libopenmpi-dev
   ```

---

## Running the Code

1. Save the script (e.g., `mpi_sum.py`).

2. Run the script using an MPI command. Replace `N` with the number of processes:
   ```bash
   mpiexec -n N python mpi_sum.py
   ```

3. Example Output:
   - Master process computes its local sum and prints:
     ```
     Master calculated integer sum is X
     ```
   - Each worker process reports its local sum:
     ```
     Received integer sum of Y from worker of rank Z
     ```
   - The total sum is computed by the master.

---

## Code Breakdown

### Key Components:

1. **Initialization**:
   - Sets up MPI communication with `MPI.COMM_WORLD`.
   - `size`: Number of processes.
   - `rank`: Current process ID.

2. **Array Division**:
   - The master process divides the array into `size` chunks.
   - Each process gets one chunk for computation.

3. **Communication**:
   - Master uses `comm.Send` to distribute chunks to workers.
   - Workers use `comm.Recv` to receive chunks and send results back with `comm.Send`.

4. **Final Aggregation**:
   - The master aggregates all partial sums to compute the total.

---

## Notes

- Ensure the array size is divisible by the number of processes for equal chunking.
- Modify the `work_array` definition to adjust the input range.
- The program uses integer data types for computation. Adjust the type if using floating-point numbers.

---

## Example Use Case

- **Summation of Large Datasets**:
   - This code can be adapted for other operations like finding maximum, minimum, or average values in large datasets by modifying the worker logic.

---

## Contribution

Feel free to contribute! Fork the repository, make your changes, and submit a pull request.

---

## License

This project is licensed under the MIT License.

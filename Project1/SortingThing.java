//Analysis of Algorithms - CSCI 323 or 700
//Assignment Number 1
//Benjamin Kluger
//WEBSITES USED 
//https://www.geeksforgeeks.org/quick-sort/
//https://www.techiedelight.com/hybrid-quicksort/
//https://www.youtube.com/watch?v=lp0xQXUEw-k

/**
 * @Description This program creates six arrays filled with random integers. 3 arrays are created with 100, 1000, and 10000 elements, 
 * all with a low pivot (for quicksort). The other three are exactly the same, yet they have a random pivot. 
 * When (high - low) < 10, the quicksort instead makes use of insertion sort. 
 * After the program runs, it prints out both the time (in nano seconds) of the each sort, as well as 
 * the number of comparisons completed. The program also prints the output to a CSV file for easy viewing.
 * 
 * @Author Ben Kluger
 * @Date 07/15/2021
 */

import java.util.*;
import javax.swing.JOptionPane;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.PrintWriter;

public class SortingThing {
	// initialize theglobal count
	static int count;

	static void random(int arr[], int low, int high) {

		Random rand = new Random();
		int pivot = rand.nextInt(high - low) + low;

		int temp1 = arr[pivot];
		arr[pivot] = arr[high];
		arr[high] = temp1;
	}

	static int partition(int[] arr, int low, int high, String whatYouWant, int n) {

		// declare and initialize a min, max, and pivot
		int min = 0;
		int max = 0;

		// choose a min/max for our random pivot
		if (n == 100) {
			min = 0;
			max = 99;
			count++;
		}

		else if (n == 1000) {
			min = 0;
			max = 999;
			count += 2;
		}

		else if (n == 10000) {
			min = 0;
			max = 9999;
			count += 3;
		} else
			count += 3; // this is for the case where n != to any of those numbers.

		// This tests for what type of pivot you want. "High" functionality is included
		if (whatYouWant == "low") {
			int pivot = low;
			swap(arr, low, high);
			count++;
		} else if (whatYouWant == "rand") {
			// pivot is chosen randomly
			random(arr, low, high);
			count += 2;
		} else
			count += 2; // this is for the case where n != to any of those.

		// Sets the pivot
		int pivot = arr[high];
		// System.out.println("The pivot is: " + pivot);

		int i = (low - 1); // index of smaller element
		for (int j = low; j < high; j++) {
			count++;
			// If current element is smaller than or
			// equal to pivot
			if (arr[j] < pivot) {
				count++;
				i++;

				// swap arr[i] and arr[j]
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
			count++; // this is to account for the final check of the if statement
		}
		count++; // this is to account for the final check of the for loop

		// swap arr[i+1] and arr[high] (or pivot)
		int temp = arr[i + 1];
		arr[i + 1] = arr[high];
		arr[high] = temp;

		return i + 1;
	}

	/*
	 * The main function that implements QuickSort arr[] --> Array to be sorted, low
	 * --> Starting index, high --> Ending index
	 */
	static void quickSort(int[] arr, int low, int high, String whichPivot, int sizeOfArray, int threshold) {
		if (low < high) {
			count++;

			// pi is partitioning index, arr[p]
			// is now at right place
			if ((high - low) < threshold) {
				insertionSort(arr, low, high);
				count++;
				return;
			}

			count++; // this is to account for the final check of the if statement
			int pi = partition(arr, low, high, whichPivot, sizeOfArray);

			// Separately sort elements before
			// partition and after partition
			quickSort(arr, low, pi - 1, whichPivot, sizeOfArray, threshold);
			quickSort(arr, pi + 1, high, whichPivot, sizeOfArray, threshold);
		}
		count++; // this is to account for the final check of the if statement
	}

	// Function to print an array
	static void printArray(int[] arr, int size) {
		for (int i = 0; i < size; i++) {
			System.out.print(arr[i] + " ");
			count++;
		}

		count++; // this is to account for the final check of the for loop
		System.out.println();
	}

	public static void insertionSort(int[] arr, int low, int n) {
		// Start from the second element (the element at index 0
		// is already sorted)
		// System.out.println("Using insertion now: ");
		for (int i = low + 1; i <= n; i++) {
			count++;
			int value = arr[i];
			int j = i;

			// find index `j` within the sorted subset `arr[0…i-1]`
			// where element `arr[i]` belongs
			while (j > low && arr[j - 1] > value) {
				count++;
				arr[j] = arr[j - 1];
				j--;
			}
			count++; // this is to account for the final check of the while loop

			// note that subarray `arr[j…i-1]` is shifted to
			// the right by one position, i.e., `arr[j+1…i]`

			arr[j] = value;
		}
		count++; // this is to account for the final check of the for loop
	}

	public static void swap(int[] array, int i, int j) {
		int temp = array[j];
		array[j] = array[i];
		array[i] = temp;
	}

	// This prints the results to a CSV file
	public static void printToCSV(String arrayName, String pivotType, int threshold, long time, int comparisons, String filepath) {
		try {
			FileWriter fw = new FileWriter(filepath, true);
			BufferedWriter bw = new BufferedWriter(fw);
			PrintWriter pw = new PrintWriter(bw);

			pw.println(arrayName + "," + pivotType + "," + threshold + "," + time + "," + comparisons);
			pw.flush();
			pw.close();

			JOptionPane.showMessageDialog(null, "Record saved");
		}

		catch (Exception E) {
			JOptionPane.showMessageDialog(null, "Record not saved");
		}
	}

	// This prints the table titles to the CSV file
	public static void printCSVTitles(String arrayName, String pivotType, String insertionThreshold, String time, String numOfComparisons,
			String filepath) {
		try {
			FileWriter fw = new FileWriter(filepath, true);
			BufferedWriter bw = new BufferedWriter(fw);
			PrintWriter pw = new PrintWriter(bw);

			pw.println(arrayName + "," + pivotType + "," + insertionThreshold + "," + time + "," + numOfComparisons);
			pw.flush();
			pw.close();

			JOptionPane.showMessageDialog(null, "Record saved");
		}

		catch (Exception E) {
			JOptionPane.showMessageDialog(null, "Record not saved");
		}
	}

	public static void main(String[] args) {

		////// PRINT TITLES//////
		printCSVTitles("Array Name", "Type of Pivot", "Threshold for Insertion Sort", "Average Time Over Ten Tests (in nanoseconds)",
				"Average Comparisons Over Ten Tests", "testResults.csv");

		String filepath = "testResults.csv";
		long begin, end;
		long t1 = 0;
		int count1 = 0, count2 = 0, count3 = 0; // low, 0
		int count4 = 0, count5 = 0, count6 = 0; // rand, 0

		int count7 = 0, count8 = 0, count9 = 0; // low, 10
		int count10 = 0, count11 = 0, count12 = 0; // rand, 10

		int count13 = 0, count14 = 0, count15 = 0; // low, 25
		int count16 = 0, count17 = 0, count18 = 0; // rand, 25

		int count19 = 0, count20 = 0, count21 = 0; // low, 50
		int count22 = 0, count23 = 0, count24 = 0; // rand, 50

		System.out.println("////START HERE////");

		// Declare all six arrays, 0
		int[] arr1 = new int[100]; // low with 100, 0
		int[] arr2 = new int[1000]; // low with 1000, 0
		int[] arr3 = new int[10000]; // low with 10000, 0

		int[] arr4 = new int[100]; // rand with 100, 0
		int[] arr5 = new int[1000]; // rand with 1000, 0
		int[] arr6 = new int[10000]; // rand with 10000, 0

		// Declare all six arrays, 10
		int[] arr7 = new int[100]; // low with 100, 10
		int[] arr8 = new int[1000]; // low with 1000, 10
		int[] arr9 = new int[10000]; // low with 10000, 10

		int[] arr10 = new int[100]; // rand with 100, 10
		int[] arr11 = new int[1000]; // rand with 1000, 10
		int[] arr12 = new int[10000]; // rand with 10000, 10

		// Declare all six arrays, 25
		int[] arr13 = new int[100]; // low with 100, 25
		int[] arr14 = new int[1000]; // low with 1000, 25
		int[] arr15 = new int[10000]; // low with 10000, 25

		int[] arr16 = new int[100]; // rand with 100, 25
		int[] arr17 = new int[1000]; // rand with 1000, 25
		int[] arr18 = new int[10000]; // rand with 10000, 25

		// Declare all six arrays, 50
		int[] arr19 = new int[100]; // low with 100, 50
		int[] arr20 = new int[1000]; // low with 1000, 50
		int[] arr21 = new int[10000]; // low with 10000, 50

		int[] arr22 = new int[100]; // rand with 100, 50
		int[] arr23 = new int[1000]; // rand with 1000, 50
		int[] arr24 = new int[10000]; // rand with 10000, 50

		int max = 99999;
		int min = 1;

		long arr1avg = 0, arr2avg = 0, arr3avg = 0; // low, 0
		long arr4avg = 0, arr5avg = 0, arr6avg = 0; // rand, 0

		long arr7avg = 0, arr8avg = 0, arr9avg = 0; // low, 10
		long arr10avg = 0, arr11avg = 0, arr12avg = 0; // rand, 10

		long arr13avg = 0, arr14avg = 0, arr15avg = 0; // low, 25
		long arr16avg = 0, arr17avg = 0, arr18avg = 0; // rand, 25

		long arr19avg = 0, arr20avg = 0, arr21avg = 0; // low, 50
		long arr22avg = 0, arr23avg = 0, arr24avg = 0; // rand, 50

		// TESTING START
		// perform Quicksort 10 times and take an average
		for (int i = 0; i < 10; i++) {

			// This section fills up all six arrays

			//////LOW SECTION////// 0 THRESHOLD
			// arr1 = low
			for (int j = 0; j < 100; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr1[j] = randomInt;
			}

			for (int j = 0; j < 1000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr2[j] = randomInt;
			}

			for (int j = 0; j < 10000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr3[j] = randomInt;
			}

			/////// RAND SECTION/////// 0 THRESHOLD
			// arr4 = rand
			for (int j = 0; j < 100; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr4[j] = randomInt;
			}

			for (int j = 0; j < 1000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr5[j] = randomInt;
			}

			for (int j = 0; j < 10000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr6[j] = randomInt;
			}
/////////////////
			//////LOW SECTION////// 10 THRESHOLD
			// arr7 = low
			for (int j = 0; j < 100; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr7[j] = randomInt;
			}

			for (int j = 0; j < 1000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr8[j] = randomInt;
			}

			for (int j = 0; j < 10000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr9[j] = randomInt;
			}

			/////// RAND SECTION/////// 10 THRESHOLD
			// arr10 = rand
			for (int j = 0; j < 100; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr10[j] = randomInt;
			}

			for (int j = 0; j < 1000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr11[j] = randomInt;
			}

			for (int j = 0; j < 10000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr12[j] = randomInt;
			}
/////////////////
			//////LOW SECTION////// 25 THRESHOLD
			// arr13 = low
			for (int j = 0; j < 100; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr13[j] = randomInt;
			}

			for (int j = 0; j < 1000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr14[j] = randomInt;
			}

			for (int j = 0; j < 10000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr15[j] = randomInt;
			}

			/////// RAND SECTION/////// 25 THRESHOLD
			// arr16 = rand
			for (int j = 0; j < 100; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr16[j] = randomInt;
			}

			for (int j = 0; j < 1000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr17[j] = randomInt;
			}

			for (int j = 0; j < 10000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr18[j] = randomInt;
			}
/////////////////
			//////LOW SECTION////// 50 THRESHOLD
			// arr19 = low
			for (int j = 0; j < 100; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr19[j] = randomInt;
			}

			for (int j = 0; j < 1000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr20[j] = randomInt;
			}

			for (int j = 0; j < 10000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr21[j] = randomInt;
			}

			/////// RAND SECTION/////// 50 THRESHOLD
			// arr22 = rand
			for (int j = 0; j < 100; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr22[j] = randomInt;
			}

			for (int j = 0; j < 1000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr23[j] = randomInt;
			}

			for (int j = 0; j < 10000; j++) {
				int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
				arr24[j] = randomInt;
			}

			// System.out.println(arr1);
			// System.out.println("Before Sort");
			// printArray(arr1, 100);
			// System.out.println("After Sort");
			// printArray(arr1, 100);

			// This is the actual sorting section

			//////LOW SECTION////// 0 THRESHOLD

			// 100, low, 0
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr1, 0, 99, "low", 100, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr1avg += t1; // set the average value
			count1 += count; // set the count1

			// 1000, low, 0
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr2, 0, 999, "low", 1000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr2avg += t1;
			count2 += count;

			// 10000, low, 0
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr3, 0, 9999, "low", 10000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr3avg += t1;
			count3 += count;

			/////// RAND SECTION/////// 0 THRESHOLD

			// 100, rand, 0
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr4, 0, 99, "rand", 100, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr4avg += t1; // set the average value
			count4 += count; // set the count1

			// 1000, rand, 0
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr5, 0, 999, "rand", 1000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr5avg += t1;
			count5 += count;

			// 10000, rand, 0 
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr6, 0, 9999, "rand", 10000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr6avg += t1;
			count6 += count;



/////////////////////////////////

//////LOW SECTION////// 10 THRESHOLD

			// 100, low, 10
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr7, 0, 99, "low", 100, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr7avg += t1; // set the average value
			count7 += count; // set the count1

			// 1000, low, 10
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr8, 0, 999, "low", 1000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr8avg += t1;
			count8 += count;

			// 10000, low, 10
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr9, 0, 9999, "low", 10000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr9avg += t1;
			count9 += count;

			/////// RAND SECTION/////// 10 THRESHOLD

			// 100, rand, 10
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr10, 0, 99, "rand", 100, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr10avg += t1; // set the average value
			count10 += count; // set the count1

			// 1000, rand, 10
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr11, 0, 999, "rand", 1000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr11avg += t1;
			count11 += count;

			// 10000, rand, 10 
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr12, 0, 9999, "rand", 10000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr12avg += t1;
			count12 += count;


/////////////////////////////////

//////LOW SECTION////// 25 THRESHOLD

			// 100, low, 25
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr13, 0, 99, "low", 100, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr13avg += t1; // set the average value
			count13 += count; // set the count1

			// 1000, low, 25
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr14, 0, 999, "low", 1000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr14avg += t1;
			count14 += count;

			// 10000, low, 25
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr15, 0, 9999, "low", 10000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr15avg += t1;
			count15 += count;

			/////// RAND SECTION/////// 25 THRESHOLD

			// 100, rand, 25
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr16, 0, 99, "rand", 100, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr16avg += t1; // set the average value
			count16 += count; // set the count1

			// 1000, rand, 25
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr17, 0, 999, "rand", 1000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr17avg += t1;
			count17 += count;

			// 10000, rand, 25 
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr18, 0, 9999, "rand", 10000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr18avg += t1;
			count18 += count;



/////////////////////////////////

//////LOW SECTION////// 50 THRESHOLD

			// 100, low, 50
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr19, 0, 99, "low", 100, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr19avg += t1; // set the average value
			count19 += count; // set the count1

			// 1000, low, 50
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr20, 0, 999, "low", 1000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr20avg += t1;
			count20 += count;

			// 10000, low, 50
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr21, 0, 9999, "low", 10000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr21avg += t1;
			count21 += count;

			/////// RAND SECTION/////// 50 THRESHOLD

			// 100, rand, 50
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr22, 0, 99, "rand", 100, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr22avg += t1; // set the average value
			count22 += count; // set the count1

			// 1000, rand, 50
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr23, 0, 999, "rand", 1000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr23avg += t1;
			count23 += count;

			// 10000, rand, 50 
			// Reset the value of count to 0
			count = 0;
			t1 = 0;
			// start the timer
			begin = System.nanoTime();
			quickSort(arr24, 0, 9999, "rand", 10000, 0);
			end = System.nanoTime(); // end the timer
			t1 += (end - begin);
			arr24avg += t1;
			count24 += count;
		}

		// n = 100
		printToCSV("n = 100", "low", 0, arr1avg / 10, count1 / 10, filepath);
		printToCSV("n = 100", "random", 0, arr4avg / 10, count4 / 10, filepath);
		printToCSV("n = 100", "low", 10, arr7avg / 10, count7 / 10, filepath);
		printToCSV("n = 100", "random", 10, arr10avg / 10, count10 / 10, filepath);
		printToCSV("n = 100", "low", 25, arr13avg / 10, count13 / 10, filepath);
		printToCSV("n = 100", "random", 25, arr16avg / 10, count16 / 10, filepath);
		printToCSV("n = 100", "low", 50, arr19avg / 10, count19 / 10, filepath);
		printToCSV("n = 100", "random", 50, arr22avg / 10, count22 / 10, filepath);

		//n = 1000
		printToCSV("n = 1000", "low", 0, arr2avg / 10, count2 / 10, filepath);
		printToCSV("n = 1000", "random", 0, arr5avg / 10, count5 / 10, filepath);
		printToCSV("n = 1000", "low", 10, arr8avg / 10, count8 / 10, filepath);
		printToCSV("n = 1000", "random", 10, arr11avg / 10, count11 / 10, filepath);
		printToCSV("n = 1000", "low", 25, arr14avg / 10, count14 / 10, filepath);
		printToCSV("n = 1000", "random", 25, arr17avg / 10, count17 / 10, filepath);
		printToCSV("n = 1000", "low", 50, arr20avg / 10, count20 / 10, filepath);
		printToCSV("n = 1000", "random", 50, arr23avg / 10, count23 / 10, filepath);

		//n = 10000
		printToCSV("n = 10000", "low", 0, arr3avg / 10, count3 / 10, filepath);
		printToCSV("n = 10000", "random", 0, arr6avg / 10, count6 / 10, filepath);
		printToCSV("n = 10000", "low", 10, arr9avg / 10, count9 / 10, filepath);
		printToCSV("n = 10000", "random", 10, arr12avg / 10, count12 / 10, filepath);
		printToCSV("n = 10000", "low", 25, arr15avg / 10, count15 / 10, filepath);
		printToCSV("n = 10000", "random", 25, arr18avg / 10, count18 / 10, filepath);
		printToCSV("n = 10000", "low", 50, arr21avg / 10, count21 / 10, filepath);
		printToCSV("n = 10000", "random", 50, arr24avg / 10, count24 / 10, filepath);


		//////Printing to console section///////

		////// LOW SECTION////// 0 THRESHOLD
		System.out.println("\n\nLOW SECTION START: \n");
		System.out.println("Array 1 Test: ");
		System.out.println("The average time taken by Quicksort: " + arr1avg / 10 + " ns");
		System.out.println("The average amount of comparisons done were: " + count1 / 10);
		

		System.out.println("Array 2 Test: ");
		System.out.println("The average time taken by Quicksort: " + arr2avg / 10 + " ns");
		System.out.println("The average amount of comparisons done were: " + count2 / 10);
		

		System.out.println("Array 3 Test: ");
		System.out.println("The average time taken by Quicksort: " + arr3avg / 10 + " ns");
		System.out.println("The average amount of comparisons done were: " + count3 / 10);
		

		////// RAND SECTION////// 0 THRESHOLD
		System.out.println("\n\nRAND SECTION START: \n");
		System.out.println("Array 4 Test: ");
		System.out.println("The average time taken by Quicksort: " + arr4avg / 10 + " ns");
		System.out.println("The average amount of comparisons done were: " + count4 / 10);
		

		System.out.println("Array 5 Test: ");
		System.out.println("The average time taken by Quicksort: " + arr5avg / 10 + " ns");
		System.out.println("The average amount of comparisons done were: " + count5 / 10);
		

		System.out.println("Array 6 Test: ");
		System.out.println("The average time taken by Quicksort: " + arr6avg / 10 + " ns");
		System.out.println("The average amount of comparisons done were: " + count6 / 10);
		
	}
}

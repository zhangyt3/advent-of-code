package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("./01.in")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var nums []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var num, err = strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println(err)
		}
		nums = append(nums, num)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// Part 1
	const want = 2020
	need := make(map[int]bool)
	for _, num := range nums {
		if _, _ok := need[num]; _ok {
			fmt.Print("Part 1: ", num*(2020-num), "\n")
			break
		}
		need[2020-num] = true
	}

	// Part 2
	fmt.Println("\nPart 2")
	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums); j++ {
			for k := 0; k < len(nums); k++ {
				if i != j && j != k {
					var total = nums[i] + nums[j] + nums[k]
					if total == want {
						fmt.Print(nums[i], nums[j], nums[k], "\n")
						fmt.Print(nums[i]*nums[j]*nums[k], "\n")
						os.Exit(0)
					}
				}
			}
		}
	}
}

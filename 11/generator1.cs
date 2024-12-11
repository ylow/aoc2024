using System;
using System.Collections.Generic;

class Program
{
    static IEnumerable<long> StoneGenerator(long stone, long step)
    {
        if (step == 0)
        {
            yield return stone;
        }
        else if (stone == 0)
        {
            foreach (var value in StoneGenerator(1, step - 1))
            {
                yield return value;
            }
        }
        else if (stone.ToString().Length % 2 == 0)
        {
            var z = stone.ToString();
            int k = z.Length / 2;
            foreach (var value in StoneGenerator(long.Parse(z.Substring(0, k)), step - 1))
            {
                yield return value;
            }
            foreach (var value in StoneGenerator(long.Parse(z.Substring(k)), step - 1))
            {
                yield return value;
            }
        }
        else
        {
            foreach (var value in StoneGenerator(stone * 2024, step - 1))
            {
                yield return value;
            }
        }
    }

    static IEnumerable<long> GenerateAll(IEnumerable<long> stoneList, long step)
    {
        foreach (var stone in stoneList)
        {
            foreach (var value in StoneGenerator(stone, step))
            {
                yield return value;
            }
        }
    }

    static void Main(string[] args)
    {
        var stoneList = new List<long> { 64599,31,674832,2659361,1,0,8867,321 };
        long nsteps = 30;
        long ctr = 0;

        foreach (var _ in GenerateAll(stoneList, nsteps))
        {
            ctr++;
            if (ctr % 1000000000 == 0) {
              Console.WriteLine(ctr);
            }
        }

        Console.WriteLine(ctr);
    }
}

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Day6 {
    public static void main(String[] args) {
        BufferedReader br = null;
        int numCoords = 50;
        int[] coordsX = new int[numCoords];
        int[] coordsY = new int[numCoords];
        int[] coordsOnEdge = new int[numCoords];
        String printBuilder = "";
        int mapSizeX = 353;
        int mapSizeY = 350;
        int[][] bigMap = new int[mapSizeX][mapSizeY];
        int largestArea = 0;
        int[] coordsArea = new int[numCoords];
        int regionSize = 0;

        try {
            br = new BufferedReader(new FileReader("input"));
            int index = 0;
            String strLine = "";
            while( (strLine = br.readLine()) != null) {
                if (!strLine.trim().isEmpty() && index < numCoords)
                    //System.out.println(strLine);
                    coordsX[index] = Integer.parseInt(strLine.substring(0, strLine.indexOf(",")));
                    coordsY[index] = Integer.parseInt(strLine.substring(strLine.indexOf(',') + 2));
                    index++;
            }
        } catch (FileNotFoundException e) {
            System.err.println("no file");
        } catch (IOException e) {
            System.err.println("unable to read file");
        }
        /*
        for (int i = 0; i < numCoords; ++i) {
            System.out.println(coordsX[i] + " " + coordsY[i]);
        }*/
        
        

        for (int i = 0; i < mapSizeY; i++) {
            for (int j = 0; j < mapSizeX; j++) {
                //bigMap[i][j] = 1;
                int shortestDist = 500;
                int coordShortest = 0;
                Boolean overlap = false;
                int totManDist = 0;
                for (int k = 0; k < numCoords; k++) {
                    int manhatDist = Math.abs(coordsX[k] - j) + Math.abs(coordsY[k] - i);
                    if (manhatDist < shortestDist) {
                        coordShortest = k;
                        shortestDist = manhatDist;
                        overlap = false;
                    } else if (manhatDist == shortestDist) {
                        overlap = true;
                    }
                    totManDist += manhatDist;
                    /*if (j == coordsX[k] && i == coordsY[k]) {
                        bigMap[j][i] = k + 1;
                    }*/
                    
                }
                if (totManDist < 10000) {
                    ++regionSize;
                }
                bigMap[j][i] = coordShortest + 1;
                    if (overlap) {
                        bigMap[j][i] = 0;
                    } else {
                        coordsArea[coordShortest] += 1;
                    }
                    if (i == 0 || j == 0 || j == mapSizeX - 1 || i == mapSizeY - 1) {
                        coordsOnEdge[coordShortest] = 1;
                        //System.out.println(j + " " + i + " Eliminated " + (coordShortest+1));
                    }

            }
        }
        
        for (int i = 0; i < numCoords; ++i) {
            if (!(coordsOnEdge[i] == 1) && coordsArea[i] > largestArea) {
                largestArea = coordsArea[i];
            }
            System.out.println(coordsOnEdge[i] + " " + coordsArea[i]);
        }
        /*
        for (int i = 0; i < mapSizeY; i++) {
            for (int j = 0; j < mapSizeX; j++) {
                printBuilder += bigMap[j][i] + " ";
            }
            printBuilder += "\n";
        }*/
        //System.out.println(printBuilder);
        System.out.println(largestArea);
        System.out.println(regionSize);
    }
}
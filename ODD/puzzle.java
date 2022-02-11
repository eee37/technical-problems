/*
    QUESTION: 
        1. Do we need to be able to re-orient puzzle pieces?
        2. Does each piece only fit with one other unique piece?
            i.e. are there identical pieces?
                if there are you may need to backtrack and determine all possible solutions
            There are 2 possible answers one where there are identical pieces
            (requires recursive backtracking solution assuming there is a unique solution)
            and one with no identical pieces (much simpler) can be solved iteratively
            focus on the second one and writing clean code
            come back to 1st one later. similar to N Queens problem
            

    * If orientation is not issue then want to start with corner pieces


    * Next piece to be added can be derived from exposed edge (type)
    
    * First Step (either before solve is called or first step)
        Can be a function called classify pieces. Maybe use a helper fxn to add corner pieces
        to solution

        * Loop over every piece and add each edge to an edge corresponding to the type.
        * Corner pieces can be added to solution (is solution an nxn matrix)?
            * Exposed edges of corner pieces can be added to an exposed array
        
    * Second Step: Determine solution
        I DON'T THINK THIS WORKS CUZ TWO EXPOSED EDGES COULD BE MATCHED WITH THE SAME PIECE
        I THINK IT WOULD MAKE THE MOST SENSE TO LOOP FOR ROWS AND COLUMNS 
        FROM THERE YOU CAN DETERMINE WHICH PIECE FITS VIA LOGIC. TODO: WRITE!

        {}{}
        {}X
        * while exposed edge 
            * Find complement that fits
            * if inner search in outer array
                * make sure exposed edge is removed from exposed
                * 
            * if outer search in inner array
    

    

*/


class Edge {

    // enum Type {

    //     inner, outer, flat

    // }

  

    Piece parent;

    Type type;

  

    boolean fitsWith(Edge edge) {
        return type == edge.Type

    }; // Inners & outer fit together.

}

enum Type {

        inner, outer, flat

}
  

class Piece {

    Edge left, right, top, bottom;

  

    // 90, 180, etc

    Orientation solvedOrientation = 90;

}

  

class Puzzle {

    // Remaining pieces left to put away.

    Piece[][] pieces;

    Piece[][] solution;

    Edge[] inners, outers, flats;

    Hashmap<Type, Edge[]> type_edge

    type_edge.add({Type.inner: inners .....})


  

    // We're going to solve this by working our way

    // in-wards, starting with the corners.

    // This is a list of the inside edges.

    Edge[] exposed_edges;

  

    void sort() {

  

        // Iterate through all edges,

        // adding each to inners, outers, etc,

        // as appropriate.

        // Look for the corners—add those to solution.

        // Add each non-flat edge of the corner

        // to exposed_edges.
        /*

        for piece in pieces:



        */

  

    }

    void addEdgetoArray(Edge edge, Type type) {
        this.map[type].add(edge)
    }

  

    void solve() {

        for (Edge edge1 : exposed_edges) {

            // Look for a match to edge1

            if (edge1.type == Edge.Type.inner) {

                for (Edge edge2 : outers) {

                    if (edge1.fitsWith(edge2)) {

                        // We found a match!

                        // Remove edge1 from

                        // exposed_edges.

                        // Add edge2's piece

                        // to solution.

                        // Check which edges of edge2

                        // are exposed, and add

                        // those to exposed_edges.

                    }

                }

                // Do the same thing,

                // swapping inner & outer.

            }

        }

    }

}
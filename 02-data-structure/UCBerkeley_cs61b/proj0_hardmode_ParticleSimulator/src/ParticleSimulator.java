import edu.princeton.cs.algs4.StdDraw;

import java.util.HashMap;
import java.util.Map;
import static org.eclipse.jetty.webapp.MetaDataComplete.False;
import static org.eclipse.jetty.webapp.MetaDataComplete.True;

public class ParticleSimulator {
    public Particle[][] particles;
    public int width;
    public int height;
    public static final Map<Character, ParticleFlavor> LETTER_TO_PARTICLE = Map.of(
            's', ParticleFlavor.SAND,
            'b', ParticleFlavor.BARRIER,
            'w', ParticleFlavor.WATER,
            'p', ParticleFlavor.PLANT,
            'f', ParticleFlavor.FIRE,
            '.', ParticleFlavor.EMPTY,
            'n', ParticleFlavor.FOUNTAIN,
            'r', ParticleFlavor.FLOWER
    );

    public ParticleSimulator(int w, int h){
        this.width = w;
        this.height = h;
        this.particles = new Particle[w][h];
        for(int i = 0; i < w; i++){
            for(int j = 0; j < h; j++){
                particles[i][j] = new Particle(ParticleFlavor.EMPTY);
            }
        }
    }

    @Override
    public String toString() {
        // 1. Build a reverse map to look up characters by Flavor
        Map<ParticleFlavor, Character> flavorToChar = new HashMap<>();
        for (Map.Entry<Character, ParticleFlavor> entry : LETTER_TO_PARTICLE.entrySet()) {
            flavorToChar.put(entry.getValue(), entry.getKey());
        }

        StringBuilder sb = new StringBuilder();

        // Have to iterate from the top so that
        // the top particles are shown first.
        for (int y = height - 1; y >= 0; y -= 1) {
            for (int x = 0; x < width; x += 1) {
                Particle p = particles[x][y];
                sb.append(flavorToChar.get(p.flavor));
            }
            sb.append("\n");
        }
        return sb.toString();
    }


    public void drawParticles() {
        for (int x = 0; x < width; x += 1) {
            for (int y = 0; y < height; y += 1) {
                StdDraw.setPenColor(particles[x][y].color());
                StdDraw.filledSquare(x, y, 0.5);
            }
        }
    }

    public boolean validIndex(int x, int y){
        if(0 <= x && x < this.width && 0 <= y && y < this.height){
            return true;
        }
        return false;
    }

    public Map<Direction, Particle> getNeighbors(int x, int y){
        Map<Direction, Particle> neighbors = new HashMap<>();
        Particle bar = new Particle(ParticleFlavor.BARRIER);
        if(x <= 0){
            neighbors.put(Direction.LEFT, bar);
        }else{
            neighbors.put(Direction.LEFT, this.particles[x-1][y]);
        }

        if(x >= this.width-1){
            neighbors.put(Direction.RIGHT, bar);
        }else{
            neighbors.put(Direction.RIGHT, this.particles[x+1][y]);
        }

        if(y <= 0){
            neighbors.put(Direction.DOWN, bar);
        }else{
            neighbors.put(Direction.DOWN, this.particles[x][y-1]);
        }

        if(y >= this.height-1){
            neighbors.put(Direction.UP, bar);
        }else{
            neighbors.put(Direction.UP, this.particles[x][y+1]);
        }

        return neighbors;
    }

    public void tick(){
        for(int i = 0; i < this.width; i++){
            for(int j = 0; j < this.height; j++){
                Map<Direction, Particle> neighbors = getNeighbors(i,j);
                this.particles[i][j].action(neighbors);
                particles[i][j].decrementLifespan();
            }
        }
    }


    static void main() {
        ParticleSimulator particleSimulator = new ParticleSimulator(150, 150);
        StdDraw.setXscale(0, particleSimulator.width);
        StdDraw.setYscale(0, particleSimulator.height);
        StdDraw.enableDoubleBuffering();
        StdDraw.clear(StdDraw.BLACK);
        ParticleFlavor nextParticleFlavor = ParticleFlavor.SAND;

        while (true) {
            if(StdDraw.hasNextKeyTyped()) {
                Character c = StdDraw.nextKeyTyped();
                nextParticleFlavor = LETTER_TO_PARTICLE.get(c);
            }
            if (StdDraw.isMousePressed()) {
                int x = (int) StdDraw.mouseX();
                int y = (int) StdDraw.mouseY();
                if(particleSimulator.validIndex(x, y)) {
                    particleSimulator.particles[x][y] = new Particle(nextParticleFlavor);
                }
            }

            particleSimulator.tick();
            particleSimulator.drawParticles();
            StdDraw.show();
            StdDraw.pause(5);
        }
    }


}

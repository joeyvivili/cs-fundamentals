import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdRandom;

import java.util.Map;
import java.awt.Color;

public class Particle {
    public static final int PLANT_LIFESPAN = 150;
    public static final int FLOWER_LIFESPAN = 75;
    public static final int FIRE_LIFESPAN = 10;
    ParticleFlavor flavor;
    int lifespan;
    public static final Map<ParticleFlavor, Integer> LIFESPANS =
            Map.of(ParticleFlavor.FLOWER, FLOWER_LIFESPAN,
                    ParticleFlavor.PLANT, PLANT_LIFESPAN,
                    ParticleFlavor.FIRE, FIRE_LIFESPAN);

    public Particle(ParticleFlavor flavor){
        this.flavor = flavor;
        if(LIFESPANS.containsKey(flavor)) {
            this.lifespan = LIFESPANS.get(flavor);
        }else{
            this.lifespan = -1;
        }
    }

    public Color color(){
        if(this.flavor == ParticleFlavor.EMPTY){
            return Color.BLACK;
        }else if(this.flavor == ParticleFlavor.SAND){
            return Color.YELLOW;
        }else if(this.flavor == ParticleFlavor.BARRIER){
            return Color.GRAY;
        }else if(this.flavor == ParticleFlavor.WATER){
            return Color.BLUE;
        }else if(this.flavor == ParticleFlavor.FOUNTAIN){
            return Color.CYAN;
        }else if(this.flavor == ParticleFlavor.PLANT){
            double ratio = (double) Math.max(0, Math.min(lifespan, PLANT_LIFESPAN)) / PLANT_LIFESPAN;
            int g = 120 + (int) Math.round((255 - 120) * ratio);
            return new Color(0, g, 0);
        }else if(this.flavor == ParticleFlavor.FIRE){
            double ratio = (double) Math.max(0, Math.min(lifespan, FIRE_LIFESPAN)) / FIRE_LIFESPAN;
            int r = (int) Math.round(255 * ratio);
            return new Color(r, 0, 0);
        }else{ // FLOWER
            double ratio = (double) Math.max(0, Math.min(lifespan, FLOWER_LIFESPAN)) / FLOWER_LIFESPAN;
            int r = 120 + (int) Math.round((255 - 120) * ratio);
            int g = 70 + (int) Math.round((141 - 70) * ratio);
            int b = 80 + (int) Math.round((161 - 80) * ratio);
            return new Color(r, g, b);
        }
    }

    void moveInto(Particle other){
        other.flavor = this.flavor;
        other.lifespan = this.lifespan;

        this.flavor = ParticleFlavor.EMPTY;
        this.lifespan = -1;
    }

    public void fall(Map<Direction, Particle> neighbors){
        Particle downNeighbor = neighbors.get(Direction.DOWN);
        if (downNeighbor.flavor == ParticleFlavor.EMPTY){
            moveInto(downNeighbor);
        }
    }

    public void action(Map<Direction, Particle> neighbors){
        if (this.flavor == ParticleFlavor.EMPTY){
            return;
        }else if(this.flavor != ParticleFlavor.BARRIER){
            fall(neighbors);
        }

        if(this.flavor == ParticleFlavor.WATER) {
            flow(neighbors);
        }

        if(this.flavor == ParticleFlavor.FLOWER || this.flavor == ParticleFlavor.PLANT){
            grow(neighbors);
        }

        if(this.flavor == ParticleFlavor.FIRE){
            burn(neighbors);
        }
    }

    public void flow(Map<Direction, Particle> neighbors){
        int chance = StdRandom.uniformInt(3);
        if(chance == 0){
            return;
        }else if(chance == 1){
            Particle leftParticle = neighbors.get(Direction.LEFT);
            if(leftParticle.flavor == ParticleFlavor.EMPTY){
                moveInto(leftParticle);
            }
        }else{
            Particle rightParticle = neighbors.get(Direction.RIGHT);
            if(rightParticle.flavor == ParticleFlavor.EMPTY){
                moveInto(rightParticle);
            }
        }
    }

    public void grow(Map<Direction, Particle> neighbors){
        int chance = StdRandom.uniformInt(10);
        if(chance == 0){
            Particle upParticle = neighbors.get(Direction.UP);
            if(upParticle.flavor == ParticleFlavor.EMPTY){
                upParticle.flavor = this.flavor;
                upParticle.lifespan = this.lifespan;    // LIFESPANS.get(this.flavor);
            }
        }else if(chance == 1){
            Particle leftParticle = neighbors.get(Direction.LEFT);
            if(leftParticle.flavor == ParticleFlavor.EMPTY){
                leftParticle.flavor = this.flavor;
                leftParticle.lifespan = this.lifespan;
            }
        }else if(chance == 2){
            Particle rightParticle = neighbors.get(Direction.RIGHT);
            if(rightParticle.flavor == ParticleFlavor.EMPTY){
                rightParticle.flavor = this.flavor;
                rightParticle.lifespan = this.lifespan;
            }
        }else{
            return;
        }
    }

    public void decrementLifespan(){
        if(this.lifespan > 0){
            this.lifespan--;
        }else if(this.lifespan == 0){
            this.flavor = ParticleFlavor.EMPTY;
            this.lifespan = -1;
        }
    }

    public void burn(Map<Direction, Particle> neighbors){
        for(Direction d: neighbors.keySet()){
            Particle neighb = neighbors.get(d);
            if(neighb.flavor == ParticleFlavor.PLANT || neighb.flavor == ParticleFlavor.FLOWER){
                int chance = StdRandom.uniformInt(10);
                if(chance < 4){
                    neighb.flavor = ParticleFlavor.FIRE;
                    neighb.lifespan = FIRE_LIFESPAN;
                }
            }
        }
    }
}


package patterns.factory;

public class Joker extends Npc {
	
	public Joker() {
		this.setForca(20);
		this.setSaude(100);
		this.setNome(NpcType.JOKER.name());
	}

}

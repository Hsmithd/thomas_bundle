# Play: Bravo - setup

- hosts: db
  become: true
  vars:
    app_name: "bravo_app"
    retry_count: 3

  tasks:
    - name: Ensure fig-task-1 is present
      ansible.builtin.file:
        path: /opt/bravo/fig-task-1
        state: directory

    - name: Template fig-task-1 config
      ansible.builtin.template:
        src: templates/fig-task-1.j2
        dest: /etc/bravo/fig-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure lima-task-2 is present
      ansible.builtin.file:
        path: /opt/bravo/lima-task-2
        state: directory

    - name: Template lima-task-2 config
      ansible.builtin.template:
        src: templates/lima-task-2.j2
        dest: /etc/bravo/lima-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart bravo service
      ansible.builtin.service:
        name: bravo
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:44Z
